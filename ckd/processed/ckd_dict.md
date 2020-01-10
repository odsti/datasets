* Data dictionary for `ckd_full.csv` and `ckd_clean.csv`

From header of `chronic_kidney_disease_full.arff` with some annotations by me (Matthew Brett), each preceded by "MB: ":

*   Age: age in years
*   Blood Pressure: : BP in mm/Hg (MB: presumably diastolic blood pressure)
*   Specific Gravity: one of (1.005,1.010,1.015,1.020,1.025); (MB: see
    <https://en.wikipedia.org/wiki/Urine_specific_gravity>)
*   Albumin: one of (0,1,2,3,4,5) (MB: in urine)
*   Sugar: one of (0,1,2,3,4,5) (MB: in urine)
*   Red Blood Cells: one of ("normal", "abnormal") (MB: in urine)
*   Pus Cell: one of ("normal", "abnormal") (MB: in urine)
*   Pus Cell clumps: one of ("present", "notpresent") (MB: in urine)
*   Bacteria: one of ("present", "notpresent") (MB: in urine)
*   Blood Glucose Random: in mgs/dl
*   Blood Urea: in mgs/dl
*   Serum Creatinine: in mgs/dl
*   Sodium: in mEq/L
*   Potassium: in mEq/L
*   Hemoglobin: in gms
*   Packed Cell Volume: (MB: volume percentage; see
    <https://en.wikipedia.org/wiki/Hematocrit>)
*   White Blood Cell Count: in cells/cumm
*   Red Blood Cell Count: in millions/cmm
*   Hypertension: one of ("yes", "no")
*   Diabetes Mellitus: one of ("yes", "no")
*   Coronary Artery Disease: one of ("yes", "no")
*   Appetite: one of ("good", "poor")
*   Pedal Edema: one of ("yes", "no")
*   Anemia: one of ("yes", "no")
*   Class : one of ("ckd", "notckd") in `ckd_full.csv`) or (1,0) in
    `ckd_clean.csv`, where 1 corresponds to "ckd").

`ckd_clean.csv` has the same data as `ckd_full.csv`, but with all rows
containing missing values dropped.  Also, the last column `Class` has a different coding, as above.
