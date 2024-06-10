from typing import Dict, List

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


def add_symptom(data: Dict, sqlite_name: str = "cliniquery.db"):
    sqlite_db = sqlite_name
    sqlite_url = f"sqlite:///{sqlite_db}"
    engine = create_engine(sqlite_url)
    session = Session(engine)

    new_question = Question(**data)
    session.add(new_question)
    session.commit()
    session.close()


if __name__ == "__main__":
    add_symptom(
        {
            "symptom": "기타 정상임신의 관리, 임신 22주 이상 ~ 34주 미만",
            "category": "Medical history",
            "subcategory": "Cervical Cancer Screening",
            "question": "When was your last Pap test for cervical cancer screening? What were the results?",
            "question_korean": "자궁경부암 검사를 마지막으로 언제하셨나요? 결과는 어땠나요?",
            "is_relevant": True,
            "source": "신촌세브란스",
            "labeler": "정윤빈 교수",
        }
    )
    add_symptom(
        {
            "symptom": "기타 정상임신의 관리, 임신 22주 이상 ~ 34주 미만",
            "category": "Medical history",
            "subcategory": "Breast Ultrasound",
            "question": "Have you ever had a breast ultrasound? When was it done and what were the results?",
            "question_korean": "유방 초음파를 촬영하신적이 있으신가요? 촬영 시점과 결과는 어땠나요?",
            "is_relevant": True,
            "source": "신촌세브란스",
            "labeler": "정윤빈 교수",
        }
    )
    add_symptom(
        {
            "symptom": "기타 정상임신의 관리, 임신 22주 이상 ~ 34주 미만",
            "category": "Medical history",
            "subcategory": "Menstrual Cycle Regularity",
            "question": "Is your menstrual cycle regular?",
            "question_korean": "생리주기는 규칙적이신 편이었나요?",
            "is_relevant": True,
            "source": "신촌세브란스",
            "labeler": "정윤빈 교수",
        }
    )
    add_symptom(
        {
            "symptom": "기타 정상임신의 관리, 임신 22주 이상 ~ 34주 미만",
            "category": "Medical history",
            "subcategory": "Menstrual Cycle Duration",
            "question": "How long does your menstrual period usually last?",
            "question_korean": "한번 생리를 할 때 기간은 어느정도인가요?",
            "is_relevant": True,
            "source": "신촌세브란스",
            "labeler": "정윤빈 교수",
        }
    )
    add_symptom(
        {
            "symptom": "기타 정상임신의 관리, 임신 22주 이상 ~ 34주 미만",
            "category": "Medical history",
            "subcategory": "Menstrual Flow Quantity",
            "question": "How heavy is your menstrual flow? Please describe it as usual, light, or heavy.",
            "question_korean": "한번 생리를 할 때 양은 어느정도인가요? 보통, 적은 편, 많은 편과 같이 말씀주시면 됩니다.",
            "is_relevant": True,
            "source": "신촌세브란스",
            "labeler": "정윤빈 교수",
        }
    )
    add_symptom(
        {
            "symptom": "기타 정상임신의 관리, 임신 22주 이상 ~ 34주 미만",
            "category": "Medical history",
            "subcategory": "Menstrual Pain",
            "question": "Do you have severe menstrual cramps?",
            "question_korean": "생리통은 심한 편인가요?",
            "is_relevant": True,
            "source": "신촌세브란스",
            "labeler": "정윤빈 교수",
        }
    )
    add_symptom(
        {
            "symptom": "기타 정상임신의 관리, 임신 22주 이상 ~ 34주 미만",
            "category": "Medical history",
            "subcategory": "Pregnancy History",
            "question": "Including the current pregnancy, how many times have you been pregnant?",
            "question_korean": "출산과 상관 없이 현재 임신 포함 총 임신 수가 어떻게 되나요?",
            "is_relevant": True,
            "source": "신촌세브란스",
            "labeler": "정윤빈 교수",
        }
    )
    add_symptom(
        {
            "symptom": "기타 정상임신의 관리, 임신 22주 이상 ~ 34주 미만",
            "category": "Medical history",
            "subcategory": "Delivery History Post 20 Weeks",
            "question": "How many deliveries have you had after 20 weeks, regardless of the newborn's survival?",
            "question_korean": "신생아의 생존유무와 상관 없이 20주 이후 분만 경험 수가 어떻게 되나요?",
            "is_relevant": True,
            "source": "신촌세브란스",
            "labeler": "정윤빈 교수",
        }
    )
    add_symptom(
        {
            "symptom": "기타 정상임신의 관리, 임신 22주 이상 ~ 34주 미만",
            "category": "Medical history",
            "subcategory": "Living Children from Birth",
            "question": "How many of your children born alive are still living?",
            "question_korean": "출산하여 생존한 자녀의 수가 어떻게 되나요?",
            "is_relevant": True,
            "source": "신촌세브란스",
            "labeler": "정윤빈 교수",
        }
    )
    add_symptom(
        {
            "symptom": "기타 정상임신의 관리, 임신 22주 이상 ~ 34주 미만",
            "category": "Medical history",
            "subcategory": "Deceased Children from Birth",
            "question": "How many of your children born alive have passed away?",
            "question_korean": "출산하여 사망한 자녀의 수가 어떻게 되나요?",
            "is_relevant": True,
            "source": "신촌세브란스",
            "labeler": "정윤빈 교수",
        }
    )
    add_symptom(
        {
            "symptom": "기타 정상임신의 관리, 임신 22주 이상 ~ 34주 미만",
            "category": "Medical history",
            "subcategory": "Early Pregnancy Loss or Low Birth Weight",
            "question": "How many times have you had a pregnancy loss before 20 weeks or delivered a baby weighing less than 500 grams?",
            "question_korean": "임신 20주 이전 또는 신생아 몸무게가 500g 이하 출산의 수가 어떻게 되나요?",
            "is_relevant": True,
            "source": "신촌세브란스",
            "labeler": "정윤빈 교수",
        }
    )
