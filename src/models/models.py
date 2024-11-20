from sqlalchemy import MetaData, Table, Column, Integer, String, Date,  Numeric

metadata = MetaData()


InsuranceRate = Table(
    "InsuranceRate",
    metadata,
    Column('id', Integer, primary_key=True, index=True), 
    Column('date', Date, nullable=False), 
    Column('cargo_type', String, nullable=False), 
    Column('rate', Numeric, nullable=False)
)