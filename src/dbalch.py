from sqlalchemy import Table, Column, Integer, REAL, create_engine, MetaData

engine = create_engine('sqlite:///sqlalchemy_example.db')
metadata = MetaData()

ipc = Table('IPC', Column('ano', Integer, primary_key=True),
            Column('ipc', REAL),
            Column('va', REAL),
            Column('rem_min', REAL),
            Column('rem_max', REAL),
            Column('pib_per_cap', REAL),
            Column('rnb_per_cap_an', REAL),
            Column('rbp_per_cap_an', REAL),
            Column('rem_per_cap', REAL))

metadata.create_all(engine)


def add_year(row):
    ipc.insert().values(row)