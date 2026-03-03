-- ============================================================
-- AI Messenger Agent - Database Initialization Script
-- ============================================================
-- Ref: Database Design §1.3 - Role-based Access Control
-- Ref: Database Design §1.5 - pgvector extension
-- ============================================================
-- Enable pgvector extension for AI embeddings
CREATE EXTENSION IF NOT EXISTS vector CASCADE;
-- Create application user role (Limited privileges)
-- Password will be overridden in production, this is for MVP/Dev
CREATE ROLE app_user WITH LOGIN PASSWORD 'app_password';
-- Grant privileges to app_user
GRANT ALL PRIVILEGES ON DATABASE messenger_agent TO app_user;
-- Set default search path
ALTER ROLE app_user
SET search_path TO public;