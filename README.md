# Scholarship
University Scholarship Allocation
1. Problem Statement
Universities may award scholarships based on academic performance,
subject-wise minimum marks, attendance, and family income. This program
evaluates each applicant against all four conditions, explains
ineligibility, and prepares a ranked merit list of eligible students.

2. Objectives
Accept subject-wise marks, attendance, and annual family income.
Validate student records and input values.
Calculate aggregate percentage.
Check aggregate, subject-wise, attendance, and income requirements.
Explain why an applicant is not eligible.
Rank eligible applicants using predefined tie-breaking rules.
3. Assumptions
The following sample policy is illustrative; change the constants in
main.py to match the university's actual rules.

Each applicant has marks in five subjects: English, Mathematics, Science,
Computer, and Social Studies.
Each subject is marked out of 100.
Aggregate percentage is the average of the five subject marks.
Minimum aggregate is 75%.
Every subject mark must be at least 60/100.
Minimum attendance is 75%.
Maximum annual family income is 250,000 currency units.
Applicants must satisfy all four criteria.
Boundary values are accepted (75 aggregate, 60 in each subject,
75 attendance, and income exactly 250,000).
The program creates a merit ranking; it does not determine scholarship
amounts or the number of awards.
4. Formulas
Aggregate percentage

Aggregate = Sum of subject marks / Number of subjects
Eligibility

Aggregate >= 75
AND every subject mark >= 60
AND Attendance >= 75
AND Annual Family Income <= 250000
5. Tie-Breaking Rules
Eligible applicants are ranked by:

Higher aggregate percentage.
If tied, higher attendance percentage.
If still tied, lower annual family income.
If still tied, student ID in ascending text order.
6. Algorithm
Start and read applicant records.
Validate unique student IDs, names, marks, attendance, and income.
Stop and display errors if any input is invalid.
Calculate each applicant's aggregate percentage.
Check the aggregate minimum.
Check every subject against the subject minimum.
Check attendance and annual family income.
Mark applicants eligible only if all conditions pass.
Record reasons for every ineligible applicant.
Collect and sort eligible applicants using the tie-break rules.
Display eligibility decisions and the final merit list.
Stop.
7. Flowchart
8. Pseudocode
START
    READ applicant records
    VALIDATE IDs, marks, attendance and income
    IF validation errors exist THEN
        DISPLAY errors
        STOP
    END IF

    FOR each applicant
        CALCULATE aggregate percentage
        CHECK aggregate minimum
        CHECK every subject minimum
        CHECK attendance minimum
        CHECK annual family income limit

        IF all conditions pass THEN
            MARK eligible
            ADD to eligible list
        ELSE
            MARK not eligible
            STORE reasons
        END IF
    END FOR

    SORT eligible applicants by:
        aggregate descending,
        attendance descending,
        income ascending,
        student ID ascending

    DISPLAY eligibility decisions and merit list
STOP
9. Python Source Code
The complete program is in main.py. It uses lists, dictionaries,
loops, conditional statements, functions, arithmetic, and sorting.

10. How to Run
Install Python 3.
Open a terminal in this project folder.
Run:
python main.py
Edit the applicants list to enter actual applicants.
Change the policy constants at the top of main.py if required.
Each applicant record contains student_id, name, marks (five marks out
of 100), attendance (percentage), and income (annual family income).

11. Sample Test Cases
Test	Input condition	Expected result
1	All four criteria satisfied	Eligible
2	Aggregate below 75%	Not eligible: aggregate
3	Any subject mark is 59	Not eligible: subject minimum
4	Attendance is 74%	Not eligible: attendance
5	Income is 250001	Not eligible: income
6	Income is exactly 250000	Income criterion passes
7	Aggregate is exactly 75%, other criteria pass	Eligible
8	Equal aggregate for two eligible applicants	Higher attendance ranks first
9	Aggregate and attendance tied	Lower income ranks first
10	All ranking fields tied	Student ID breaks the tie
11	Duplicate student ID	Validation error
12	Mark outside 0–100 or invalid attendance	Validation error
12. Sample Output
UNIVERSITY SCHOLARSHIP ALLOCATION
========================================================================
Criteria: aggregate >= 75.0%; every subject >= 60.0; attendance >= 75.0%; income <= 250000

APPLICANT ELIGIBILITY
------------------------------------------------------------------------
Aarav (U101) | Aggregate: 88.40% | Attendance: 92.0% | Income: 180000 | ELIGIBLE
Diya (U102) | Aggregate: 90.00% | Attendance: 95.0% | Income: 200000 | ELIGIBLE
Ishita (U103) | Aggregate: 80.00% | Attendance: 88.0% | Income: 150000 | ELIGIBLE
Kabir (U104) | Aggregate: 85.20% | Attendance: 96.0% | Income: 120000 | NOT ELIGIBLE
  Reason(s): Below subject minimum in Mathematics
Meera (U105) | Aggregate: 81.00% | Attendance: 72.0% | Income: 100000 | NOT ELIGIBLE
  Reason(s): Attendance below 75.0%
Rohan (U106) | Aggregate: 85.00% | Attendance: 90.0% | Income: 300000 | NOT ELIGIBLE
  Reason(s): Annual family income exceeds 250000
Sara (U107) | Aggregate: 88.40% | Attendance: 92.0% | Income: 160000 | ELIGIBLE

FINAL SCHOLARSHIP MERIT LIST
------------------------------------------------------------------------
1. Diya (U102) | Aggregate: 90.00% | Attendance: 95.0% | Annual income: 200000
2. Sara (U107) | Aggregate: 88.40% | Attendance: 92.0% | Annual income: 160000
3. Aarav (U101) | Aggregate: 88.40% | Attendance: 92.0% | Annual income: 180000
4. Ishita (U103) | Aggregate: 80.00% | Attendance: 88.0% | Annual income: 150000
13. Conclusion
The program evaluates scholarship applicants using aggregate marks,
subject-wise minimum scores, attendance, and annual family income. It
explains ineligibility and ranks eligible students consistently using
predefined tie-breaking rules, providing a transparent scholarship merit list.

