"""Initial migration (aman untuk DB lama)

Revision ID: 46f9c8eb813d
Revises: 
Create Date: 2025-04-05 15:25:36.017919

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46f9c8eb813d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # === Tabel kehadiran ===
    with op.batch_alter_table('kehadiran', schema=None) as batch_op:
        # Tambahkan kolom mahasiswa_id (sementara nullable)
        batch_op.add_column(sa.Column('mahasiswa_id', sa.Integer(), nullable=True))
        
        # (JANGAN hapus user_id dulu, agar data lama tetap aman)
        # Constraint lama bisa dibiarkan, atau jika perlu diganti manual

        # Tambahkan foreign key ke mahasiswa (bisa temporary constraint)
        batch_op.create_foreign_key('fk_kehadiran_mahasiswa', 'mahasiswa', ['mahasiswa_id'], ['id'])

    # === Tabel mahasiswa ===
    with op.batch_alter_table('mahasiswa', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=200), nullable=True))
        batch_op.add_column(sa.Column('no_telepon', sa.String(length=20), nullable=True))
        batch_op.add_column(sa.Column('mata_kuliah', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('foto_tangan_kiri', sa.String(length=200), nullable=True))
        batch_op.add_column(sa.Column('foto_tangan_kanan', sa.String(length=200), nullable=True))
        batch_op.add_column(sa.Column('foto_wajah', sa.String(length=200), nullable=True))
        
        # Jangan langsung hapus password_hash
        # Bisa dihapus setelah data dipindahkan

    # === Tabel mata_kuliah ===
    with op.batch_alter_table('mata_kuliah', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id_mk', sa.String(length=20), nullable=True))
        batch_op.alter_column('tahun_akademik',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
        
        # Jangan langsung drop constraint dan kolom lama
        # Bisa ubah id_mk jadi unique jika sudah aman
        batch_op.create_unique_constraint('uq_id_mk', ['id_mk'])


def downgrade():
    # Downgrade normal sesuai kondisi awal
    with op.batch_alter_table('mata_kuliah', schema=None) as batch_op:
        batch_op.drop_constraint('uq_id_mk', type_='unique')
        batch_op.drop_column('id_mk')
        batch_op.alter_column('tahun_akademik',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)

    with op.batch_alter_table('mahasiswa', schema=None) as batch_op:
        batch_op.drop_column('password')
        batch_op.drop_column('no_telepon')
        batch_op.drop_column('mata_kuliah')
        batch_op.drop_column('foto_tangan_kiri')
        batch_op.drop_column('foto_tangan_kanan')
        batch_op.drop_column('foto_wajah')

    with op.batch_alter_table('kehadiran', schema=None) as batch_op:
        batch_op.drop_constraint('fk_kehadiran_mahasiswa', type_='foreignkey')
        batch_op.drop_column('mahasiswa_id')
