--
-- PostgreSQL database dump
--

-- Dumped from database version 16.8
-- Dumped by pg_dump version 16.8

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: jadwal; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jadwal (
    id integer NOT NULL,
    mata_kuliah_id integer NOT NULL,
    pertemuan_ke integer NOT NULL,
    tanggal date NOT NULL,
    jam_mulai time without time zone NOT NULL,
    jam_selesai time without time zone NOT NULL
);


ALTER TABLE public.jadwal OWNER TO postgres;

--
-- Name: jadwal_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.jadwal_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.jadwal_id_seq OWNER TO postgres;

--
-- Name: jadwal_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.jadwal_id_seq OWNED BY public.jadwal.id;


--
-- Name: kehadiran; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.kehadiran (
    id integer NOT NULL,
    user_id integer NOT NULL,
    jadwal_id integer NOT NULL,
    waktu_scan timestamp without time zone NOT NULL,
    status character varying(10) NOT NULL
);


ALTER TABLE public.kehadiran OWNER TO postgres;

--
-- Name: kehadiran_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.kehadiran_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.kehadiran_id_seq OWNER TO postgres;

--
-- Name: kehadiran_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.kehadiran_id_seq OWNED BY public.kehadiran.id;


--
-- Name: mahasiswa; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mahasiswa (
    id integer NOT NULL,
    nama_lengkap character varying(100) NOT NULL,
    nim character varying(20) NOT NULL,
    email character varying(100) NOT NULL,
    password_hash character varying(128) NOT NULL
);


ALTER TABLE public.mahasiswa OWNER TO postgres;

--
-- Name: mahasiswa_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.mahasiswa_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.mahasiswa_id_seq OWNER TO postgres;

--
-- Name: mahasiswa_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.mahasiswa_id_seq OWNED BY public.mahasiswa.id;


--
-- Name: mata_kuliah; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mata_kuliah (
    id integer NOT NULL,
    kode_mk character varying(20) NOT NULL,
    nama_mk character varying(100) NOT NULL,
    semester character varying(10) NOT NULL,
    tahun_akademik character varying(20)
);


ALTER TABLE public.mata_kuliah OWNER TO postgres;

--
-- Name: mata_kuliah_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.mata_kuliah_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.mata_kuliah_id_seq OWNER TO postgres;

--
-- Name: mata_kuliah_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.mata_kuliah_id_seq OWNED BY public.mata_kuliah.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    nama_lengkap character varying(100) NOT NULL,
    nim character varying(20),
    email character varying(100) NOT NULL,
    password_hash character varying(255) NOT NULL,
    role character varying(10) NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: jadwal id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jadwal ALTER COLUMN id SET DEFAULT nextval('public.jadwal_id_seq'::regclass);


--
-- Name: kehadiran id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.kehadiran ALTER COLUMN id SET DEFAULT nextval('public.kehadiran_id_seq'::regclass);


--
-- Name: mahasiswa id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mahasiswa ALTER COLUMN id SET DEFAULT nextval('public.mahasiswa_id_seq'::regclass);


--
-- Name: mata_kuliah id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mata_kuliah ALTER COLUMN id SET DEFAULT nextval('public.mata_kuliah_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
\.


--
-- Data for Name: jadwal; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jadwal (id, mata_kuliah_id, pertemuan_ke, tanggal, jam_mulai, jam_selesai) FROM stdin;
14	1	1	2025-04-10	08:00:00	10:00:00
15	1	2	2025-04-17	08:00:00	10:00:00
16	1	3	2025-04-05	12:00:00	14:00:00
17	1	3	2025-04-05	05:00:00	06:00:00
18	1	1	2025-04-05	12:50:00	13:30:00
\.


--
-- Data for Name: kehadiran; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.kehadiran (id, user_id, jadwal_id, waktu_scan, status) FROM stdin;
\.


--
-- Data for Name: mahasiswa; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mahasiswa (id, nama_lengkap, nim, email, password_hash) FROM stdin;
\.


--
-- Data for Name: mata_kuliah; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mata_kuliah (id, kode_mk, nama_mk, semester, tahun_akademik) FROM stdin;
1	MK001	Pemrograman Lanjut	6	2024/2025
2	MK002	Jaringan Komputer	6	2024/2025
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, nama_lengkap, nim, email, password_hash, role) FROM stdin;
1	Liza Wikarza	\N	dosen@example.com	scrypt:32768:8:1$TLBjPGwbJd3rzzVF$39bf2960e0f2ba486033d1c1f6b24505d62c0399265e502e9dfffc99b4552c29c1759254931527ed74d933d3e2eb3b94b6a467301fb0e734f232e5d812114834	admin
\.


--
-- Name: jadwal_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.jadwal_id_seq', 18, true);


--
-- Name: kehadiran_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.kehadiran_id_seq', 1, true);


--
-- Name: mahasiswa_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.mahasiswa_id_seq', 1, false);


--
-- Name: mata_kuliah_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.mata_kuliah_id_seq', 3, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 2, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: jadwal jadwal_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jadwal
    ADD CONSTRAINT jadwal_pkey PRIMARY KEY (id);


--
-- Name: kehadiran kehadiran_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.kehadiran
    ADD CONSTRAINT kehadiran_pkey PRIMARY KEY (id);


--
-- Name: mahasiswa mahasiswa_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mahasiswa
    ADD CONSTRAINT mahasiswa_email_key UNIQUE (email);


--
-- Name: mahasiswa mahasiswa_nim_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mahasiswa
    ADD CONSTRAINT mahasiswa_nim_key UNIQUE (nim);


--
-- Name: mahasiswa mahasiswa_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mahasiswa
    ADD CONSTRAINT mahasiswa_pkey PRIMARY KEY (id);


--
-- Name: mata_kuliah mata_kuliah_kode_mk_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mata_kuliah
    ADD CONSTRAINT mata_kuliah_kode_mk_key UNIQUE (kode_mk);


--
-- Name: mata_kuliah mata_kuliah_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mata_kuliah
    ADD CONSTRAINT mata_kuliah_pkey PRIMARY KEY (id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_nim_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_nim_key UNIQUE (nim);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: jadwal jadwal_mata_kuliah_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jadwal
    ADD CONSTRAINT jadwal_mata_kuliah_id_fkey FOREIGN KEY (mata_kuliah_id) REFERENCES public.mata_kuliah(id);


--
-- Name: kehadiran kehadiran_jadwal_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.kehadiran
    ADD CONSTRAINT kehadiran_jadwal_id_fkey FOREIGN KEY (jadwal_id) REFERENCES public.jadwal(id);


--
-- Name: kehadiran kehadiran_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.kehadiran
    ADD CONSTRAINT kehadiran_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

