from sqlalchemy import create_engine

DATABASE_URL = (
    "postgresql://postgresadmin:Cr!2025Risk@DB#Secure@change-risk-db.postgres.database.azure.com:5432/change_risk_db"
)

engine = create_engine(
    DATABASE_URL
)