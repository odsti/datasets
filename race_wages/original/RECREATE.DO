set more 1
set maxobs 13000
set mem 12000

log using recreate, replace

/***THIS STATA PROGRAM RECREATES THE WAGE, AGE, AFQT, RACE, AND SEX
    VARIABLES USED IN  NEAL & JOHNSON (1996).   THE RESULTING DATA SET
    IS CALLED JPE96.DTA.  THE BOTTOM OF THE LOG FILE PROVIDES
    REGRESSION RESULTS THAT ARE "ALMOST" EXACTLY THE SAME AS THOSE
    REPORTED IN THE PAPER.  THE SMALL DIFFERENCES  (3 EXTRA FEMALES
    IN THE SAMPLE AND MINOR CHANGES IN COEFFICIENTS) ARE NOT DUE TO ANY
    CHANGE IN THE PROGRAM.  THEY RELFECT THE FACT THAT MORE RECENT 
    RELEASES OF THE NLSY DATA INCLUDE WAGE OBSERVATIONS THAT HAVE BEEN
    EDITED SINCE THE RELEASE OF THE 1991 FILE THAT WE USED.***/

#delimit ;


/****RECREATE.DAT IS CREATED USING THE NLSY EXTRACTION SOFTWARE.
     NOT ALL OF THE VARS IN THE EXTRACTION ARE USED IN THIS PARTICULAR
     PROGRAM.  THE 92+ WAGE AND EARNINGS WARIABLES WERE NOT AVAILABLE
     WHEN WE BEGAN WORKING ON THE PAPER.  SEE RECREATE.CDB & RECREATE.SAS
     FOR DETAILS****/



infile id month79 year79 sid race sex79 month81 year81 code hgasvab
          arith word comp numop math arithstd mathstd verbstd 
          afqt80 afqt89 sex82 class90 wage90 esr90 class91 wage91
          earn91 esr91 class92 wage92 earn92 esr92 class93 earn93
          wage93 esr93 earn94 wage94 esr94 
          using d:\nlsy\extracts\recreate.dat;


/***ONLY THE CROSS-SECTION SAMPLE & THE OVERSAMPLES OF BLACKS AND HISPANICS**/
/***DELETE MILITARY & EDW SAMPLE***/

drop if sid > 14;
drop if sid==9;
drop if sid==12;



/****GENERATE YEAR OF BIRTH USING DATA FROM TWO YEARS
     STEVE McCLASKEY OF CHRR SUGGESTED THIS RULE********/

gen year=0;
replace year=year81 if year81 > 0;
replace year=year79 if year81 <=0;


/****SET ASVAB SCORES TO -9 IF THERE ARE PROBLEMS WITH THE TEST.
     WE CAN USE THE MATH TEST AS AN INDICATOR BECAUSE RESPONDENTS
     EITHER TOOK THEM ALL OR TOOK NONE OF THEM.  FURTHER, THE
     ALTERED TESTING CODES APPLY TO THE EXAMS AS A WHOLE***/

/***NOTE ADD IN 2004:  TECHNICALLY A FEW PEOPLE TOOK ARITH WITHOUT
    TAKING THE OTHER TESTS, BUT THE CODE BELOW STILL DOES WHAT WE
    WANT BECAUSE THERE ARE NO POSITIVE MATH SCORES FOR PEOPLE WHO
    HAVE NEGATIVES ON OTHER EXAMS***/


replace math=-9      if code==53 | code==67 | math < 0;
replace arith=-9     if math ==-9;
replace comp=-9      if math ==-9;
replace word=-9      if math ==-9;
replace numop=-9     if math ==-9;
replace arithstd=-9  if math ==-9;
replace mathstd=-9   if math ==-9;
replace verbstd=-9   if math ==-9;
replace afqt80=-9    if math ==-9;
replace afqt89=-9    if math ==-9;



/**THIS IS THE SCORING SYSTEM FOR THE 1989 VERSION OF THE AFQT
   SEE THE NLS USER'S GUIDE - 1995 , p. 52********************/


gen std89=(2*verbstd) + mathstd + arithstd;
replace std89=-9     if math==-9;



/***BELOW WE CONVERT THE SCORES TO AGE STANDARDIZE SCORES
    THEREFORE, WE NEED TO MARK BAD BIRTH YEARS****/


gen badyear=0;
replace badyear=1 if year < 57 | year > 64;


/***MAKE YEAR OF BIRTH DUMMIES*****/

gen y1=0;
replace y1=1 if year==57;
gen y2=0;
replace y2=1 if year==58;
gen y3=0;
replace y3=1 if year==59;
gen y4=0;
replace y4=1 if year==60;
gen y5=0;
replace y5=1 if year==61;
gen y6=0;
replace y6=1 if year==62;
gen y7=0;
replace y7=1 if year==63;
gen y8=0;
replace y8=1 if year==64;


/*CREATE AGE ADJUSTED, STANDARD SCORES FOR CASES WITH VALID DATA.
  "std89res" IS THE VARIABLE THAT WE USED AS AN AFQT SCORE.***/

regress std89 y2 y3 y4 y5 y6 y7 y8 if math >= 0 & badyear==0;
predict std89res if math>=0 & badyear==0,rstandard;

replace std89res=-9 if std89res==.;


/*HERE, WE RECREATE OUR WAGE MEASURE***/
/****FIRST WE NEED TO CREATE AN EMPLOYMENT STATUS VARIABLE***/
/****STATUS=1 - RESP. IS WORKING - VALID ENTRY FOR "CLASS OF WORKER."
     STATUS=0 - RESP. IS NOT WORKING - VALID SKIP FOR "CLASS OF WORKER"
                                      AND NOT IN THE MILITARY****/

/****STATUS=-9 - THE REPSONDENT IS IN THE MILITARY OR
            THE RESPONDENT'S WAGE DATA IS MISSING DUE TO CODING PROBLEMS***/

gen st90=-9;
replace st90=1 if class90 > 0;
replace st90=0 if class90==-4 & esr90~=8;

gen st91=-9;
replace st91=1 if class91 > 0;
replace st91=0 if class91==-4 & esr91~=8;


/***NOW EDIT THE WAGE DATA*******************************/
/** IF HOURLY WAGE EXCEEDS $75, THEN LABEL IT INVALID.
    BELOW, THE SAME RULE APPLIES FOR WAGES < $1****/


replace wage90=-9 if wage90>7500;
replace wage91=-9 if wage91>7500;


/*CREATE FLAGS FOR RESP. WHO BELONG IN THE SAMPLE FOR MEDIAN
  REGRESSIONS.  THEY MUST HAVE A VALID WAGE OBSERVATION or 
  ST** = 0 IN AT LEAST ONE YEAR.  WE DO NOT TREAT
  PERSONS WITH BAD WAGE OBSERV OR STATUS=-9 AS NON-PARTICPANTS*/


gen flag=0;
replace flag=1 if st90==0;
replace flag=1 if st91==0;


/*WAGE=1 FOR THE NON-VALID WAGE RECORDS & NON-PARTICPANTS. THIS IS 
  OKAY BECAUSE THERE IS NO ONE WHO EARNS ONE CENT PER HOUR.
  THUS logwage=0 FOR BOTH NON-PARTICIPANTS AND CODING ERRORS*/


gen wage=1;   /*if both wage obs are < 100 */
replace wage=(wage91/1.04) if wage90 <= 100 & wage91 > 100;  /*CPI*/
replace wage=wage90 if wage91 <= 100 & wage90 > 100;
replace wage=((wage90 + (wage91/1.04))/2) if wage90 > 100 & wage91 > 100;


replace wage=1 if st90==0 & st91==0;   /*mitigates coding error problem*/

replace flag=1 if wage > 1;


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



/**CREATE VARIABLES USED IN THE PAPER**********************/

gen lwage=log(wage);

gen age=90-year;


gen hisp=0;
replace hisp=1 if race==1;
gen black=0;
replace black=1 if race==2;


gen female=0;
replace female=1 if sex82==2;
replace female=1 if sex82 < 0 & sex79==2;


gen a1=std89res;
gen a2=a1*a1;


/**CREATE SAMPLE IDENTIFIES.  INSAMP1 = VALID FOR OLS REGRESSIONS.
                              INSAMP2 = VALID FOR MEDIAN REGRESSIONS.**/

gen insamp1=0;
replace insamp1=1 if lwage > 0 & math >= 0 & year > 61 & badyear==0;

gen insamp2=0;
replace insamp2=1 if flag==1 & math >= 0  & year > 61 & badyear==0;



/***THESE REGRESSION REPLICATE KEY COLUMNS OF TABLE 1 & TABLE 4.****/


regress lwage black hisp age if insamp1==1 & female==0;

regress lwage black hisp age a1 a2 if insamp1==1 & female==0;

qreg lwage black hisp age if insamp2==1 & female==0;

qreg lwage black hisp age a1 a2 if insamp2==1 & female==0;


regress lwage black hisp age if insamp1==1 & female==1;

regress lwage black hisp age a1 a2 if insamp1==1 & female==1;


/***THE KEEP STATEMENT GIVES THE VARIABLES USED IN OUR BASIC
    WAGE REGRESSIONS PLUS SAMPLE INDETIFIERS AND RELATED TESTS
    SCORE ITEMS.  NOTE: afqt80 & afqt89 ARE PERCENTILE SCORES.**/


keep id sid female black hisp year age insamp1 insamp2 badyear
     wage90 wage91 st90 st91 flag lwage
     afqt80 afqt89 std89 std89res math arith word comp numop;


sum if insamp1==1;



save d:\nlsy\data\JPE96,replace;



log close;

clear;
