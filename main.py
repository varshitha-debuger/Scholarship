"""
University Scholarship Allocation
Evaluates applicants by aggregate marks, subject minimums, attendance,
and annual family income; ranks eligible applicants with tie-break rules.
"""

MIN_AGGREGATE = 75.0
MIN_SUBJECT_MARK = 60.0
MIN_ATTENDANCE = 75.0
MAX_ANNUAL_INCOME = 250000.0
SUBJECTS = ["English", "Mathematics", "Science", "Computer", "Social Studies"]

# Marks are out of 100; income is annual family income.
applicants = [
    {"student_id": "U101", "name": "Aarav", "marks": [88, 92, 85, 90, 87], "attendance": 92, "income": 180000},
    {"student_id": "U102", "name": "Diya", "marks": [90, 90, 90, 90, 90], "attendance": 95, "income": 200000},
    {"student_id": "U103", "name": "Ishita", "marks": [78, 82, 75, 80, 85], "attendance": 88, "income": 150000},
    {"student_id": "U104", "name": "Kabir", "marks": [95, 58, 90, 92, 91], "attendance": 96, "income": 120000},
    {"student_id": "U105", "name": "Meera", "marks": [80, 82, 78, 85, 80], "attendance": 72, "income": 100000},
    {"student_id": "U106", "name": "Rohan", "marks": [85, 85, 85, 85, 85], "attendance": 90, "income": 300000},
    {"student_id": "U107", "name": "Sara", "marks": [88, 92, 85, 90, 87], "attendance": 92, "income": 160000},
]


def validate_applicants(records):
    errors = []
    seen_ids = set()

    if not records:
        return ["No applicant records were provided."]

    for applicant in records:
        sid = applicant.get("student_id")
        if not sid:
            errors.append("Missing student ID.")
        elif sid in seen_ids:
            errors.append("Duplicate student ID: " + str(sid))
        else:
            seen_ids.add(sid)

        if not applicant.get("name"):
            errors.append("Missing name for student: " + str(sid))

        marks = applicant.get("marks")
        if not isinstance(marks, list) or len(marks) != len(SUBJECTS):
            errors.append("Student {} must have exactly {} subject marks.".format(sid, len(SUBJECTS)))
        else:
            for mark in marks:
                if not isinstance(mark, (int, float)) or not 0 <= mark <= 100:
                    errors.append("Invalid subject mark for student: " + str(sid))
                    break

        attendance = applicant.get("attendance")
        if not isinstance(attendance, (int, float)) or not 0 <= attendance <= 100:
            errors.append("Invalid attendance for student: " + str(sid))

        income = applicant.get("income")
        if not isinstance(income, (int, float)) or income < 0:
            errors.append("Invalid annual income for student: " + str(sid))

    return errors


def evaluate_applicant(applicant):
    aggregate = sum(applicant["marks"]) / len(applicant["marks"])
    failed_subjects = []

    for index in range(len(applicant["marks"])):
        if applicant["marks"][index] < MIN_SUBJECT_MARK:
            failed_subjects.append(SUBJECTS[index])

    reasons = []
    if aggregate < MIN_AGGREGATE:
        reasons.append("Aggregate below {:.1f}%".format(MIN_AGGREGATE))
    if failed_subjects:
        reasons.append("Below subject minimum in " + ", ".join(failed_subjects))
    if applicant["attendance"] < MIN_ATTENDANCE:
        reasons.append("Attendance below {:.1f}%".format(MIN_ATTENDANCE))
    if applicant["income"] > MAX_ANNUAL_INCOME:
        reasons.append("Annual family income exceeds {:.0f}".format(MAX_ANNUAL_INCOME))

    return {
        "student_id": applicant["student_id"],
        "name": applicant["name"],
        "aggregate": aggregate,
        "attendance": applicant["attendance"],
        "income": applicant["income"],
        "eligible": len(reasons) == 0,
        "reasons": reasons
    }


def rank_eligible_applicants(eligible):
    # Higher aggregate, higher attendance, lower income, then student ID.
    return sorted(
        eligible,
