from typing import List

from sqlmodel import Sequence, Session, create_engine, select

from models import Patient, Question


def load_patients(sqlite_name: str = "cliniquery.db") -> Sequence[Patient]:
    sqlite_db = sqlite_name
    sqlite_url = f"sqlite:///{sqlite_db}"
    engine = create_engine(sqlite_url)
    session = Session(engine)

    query_for_patient = select(Patient)
    patients = session.exec(query_for_patient).all()

    session.close()

    return patients


def add_symptom(symptom: str, sqlite_name: str = "cliniquery.db"):
    sqlite_db = sqlite_name
    sqlite_url = f"sqlite:///{sqlite_db}"
    engine = create_engine(sqlite_url)
    session = Session(engine)

    new_question = Question(symptom=symptom)
    session.add(new_question)
    session.commit()
    session.close()


if __name__ == "__main__":
    add_symptom("기타 정상임신의 관리, 임신 22주 이상 ~ 34주 미만")
