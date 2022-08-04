set more 1

log using race_wages.log, replace

import delimited using processed/race_wages

/* Replicate calculation of residuals */

/***MAKE YEAR OF BIRTH DUMMIES*****/

gen y1=0
replace y1=1 if year==57
gen y2=0
replace y2=1 if year==58
gen y3=0
replace y3=1 if year==59
gen y4=0
replace y4=1 if year==60
gen y5=0
replace y5=1 if year==61
gen y6=0
replace y6=1 if year==62
gen y7=0
replace y7=1 if year==63
gen y8=0
replace y8=1 if year==64


/*CREATE AGE ADJUSTED, STANDARD SCORES FOR CASES WITH VALID DATA.
  "std89res" IS THE VARIABLE THAT WE USED AS AN AFQT SCORE.***/

regress std89 y2 y3 y4 y5 y6 y7 y8 if math >= 0 & badyear==0
predict std89res_recalc if math>=0 & badyear==0,rstandard

replace std89res_recalc=-9 if std89res_recalc==.

/***NOW EDIT THE WAGE DATA*******************************/
/** IF HOURLY WAGE EXCEEDS $75, THEN LABEL IT INVALID.
    BELOW, THE SAME RULE APPLIES FOR WAGES < $1****/

/*BECAUSE ST90 & ST91 WERE CREATED FROM THE CLASS OF WORKER
  VARIABLE, IT IS POSSIBLE TO GET ST90(91)=-9 & WAGE90(91) > 1 FOR INVALID
  SKIPS ON THE CLASS VARIABLE.  HOWEVER THE ST90(91)==0 & WAGE90(91) > 1
  CASES ARE MORE OF A PUZZLE.  KARIMA NAGEE (CHRR) CLAIMS THESE (TWO)
  CASES ARE LIKELY CODING ERROR.  THUS, IN THE CASE WHERE BOTH
  STATUS VARIABLES ARE ZERO, WE SET THE WAGE=0.

  ON THE OTHER HAND, THERE ARE APPROX. 380 PEOPLE IN
  THE 1990 SURVEY & A SIMILAR NUMBER IN 1991 WHO ARE A VAILD SKIP
  FOR WAGES BUT ACTUALLY REPORT A VALID CLASS OF WORKER.  THESE
  PEOPLE ARE EMPLOYED BUT GAVE BAD OR INCOMPLETE WAGE INFORMATION.*/

gen a1=std89res
gen a2=a1*a1


/***THESE REGRESSION REPLICATE KEY COLUMNS OF TABLE 1 & TABLE 4.****/


regress lwage black hisp age if insamp1==1 & female==0

regress lwage black hisp age a1 a2 if insamp1==1 & female==0

qreg lwage black hisp age if insamp2==1 & female==0

qreg lwage black hisp age a1 a2 if insamp2==1 & female==0


regress lwage black hisp age if insamp1==1 & female==1

regress lwage black hisp age a1 a2 if insamp1==1 & female==1

sum if insamp1==1

log close

clear
