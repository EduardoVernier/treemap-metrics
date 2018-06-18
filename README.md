datasets="bdb
pybuilder
hiv
Hystrix
exo
beets
AudioKit
animate.css
poly
m-names
standard"
for d in $datasets; do echo $d; time python3 Main.py kde-ct $d; time python3 Main.py kde-rpc $d; done
for d in $datasets; do echo $d; time python3 Main.py kde-rpc $d; time python3 Main.py kde-rpc $d; done
for d in $datasets; do echo $d; time python3 Main.py boxplots $d; done

datasets="calcuta
emcee
exports
iina
PhysicsJS
shellcheck"
for d in $datasets; do time python3 Main.py cache-metrics $d; done

python3 Main.py scatter bdb pybuilder hiv Hystrix exo beets AudioKit animate.css poly m-names standard calcuta emcee exports iina PhysicsJS shellcheck;

python3 Main.py matrix bdb pybuilder hiv Hystrix exo beets AudioKit animate.css poly m-names standard calcuta emcee exports iina PhysicsJS shellcheck


15Months1DayRating.csv
datasets="3Years3MonthRating.csv
Hierarchy22Year7Month.csv
HierarchyCumulative9Year1Week.csv
HierarchyCumulative9Year7Month.csv
Cumulative4Year90HoursRating.csv
Cumulative10Years2MonthRating.csv"
for d in $datasets; do echo $d; time python3 Main.py cache-metrics $d; done

datasets="Cumulative4Year90HoursRating.csv
m-names
15Months1DayRating.csv
Cumulative10Years2MonthRating.csv
hiv
3Years3MonthRating.csv
standard
HierarchyCumulative9Year7Month.csv
Hierarchy22Year7Month.csv
HierarchyCumulative9Year1Week.csv
Hystrix"
for d in $datasets; do echo $d; time python3 Main.py kde-ct $d; time python3 Main.py kde-rpc $d; done; for d in $datasets; do echo $d; time python3 Main.py kde-rpc $d; time python3 Main.py kde-rpc $d; done; for d in $datasets; do echo $d; time python3 Main.py boxplots $d; done


1 Liner
python3 Main.py matrix Cumulative4Year90HoursRating.csv m-names 15Months1DayRating.csv Cumulative10Years2MonthRating.csv hiv 3Years3MonthRating.csv standard HierarchyCumulative9Year7Month.csv Hierarchy22Year7Month.csv HierarchyCumulative9Year1Week.csv Hystrix

python3 Main.py scatter Cumulative4Year90HoursRating.csv m-names 15Months1DayRating.csv Cumulative10Years2MonthRating.csv hiv 3Years3MonthRating.csv standard HierarchyCumulative9Year7Month.csv Hierarchy22Year7Month.csv HierarchyCumulative9Year1Week.csv Hystrix


{'Cumulative4Year90HoursRating.csv' : 'Movies C4Y90H',
'm-names' : 'Dutch Names',
'15Months1DayRating.csv': '15M1D',
'Cumulative10Years2MonthRating.csv' : 'Movies C10Y2M',
'hiv' : 'World Bank HIV',
'3Years3MonthRating.csv' : 'Movies 3y3M',
'standard' : 'GitHub standard',
'HierarchyCumulative9Year7Month.csv' : 'Movies HC9Y7M',
'Hierarchy22Year7Month.csv' : 'Movies H22Y7M',
'HierarchyCumulative9Year1Week.csv' : 'Movies HC9Y1W',
'Hystrix' : 'GitHub Hystrix'}


datasets="m-names
Cumulative10Years2MonthRating.csv
hiv
3Years3MonthRating.csv
standard
HierarchyCumulative9Year7Month.csv
Hierarchy22Year7Month.csv
HierarchyCumulative9Year1Week.csv
Hystrix
15Months1DayRating.csv
Cumulative4Year90HoursRating.csv"

datasets="m-names
Cumulative10Years2MonthRating.csv
hiv
3Years3MonthRating.csv
standard
HierarchyCumulative9Year7Month.csv
Hierarchy22Year7Month.csv
HierarchyCumulative9Year1Week.csv
Hystrix
15Months1DayRating.csv
Cumulative4Year90HoursRating.csv"

for d in $datasets; do echo $d; time python3 Main.py boxplots $d; done

0 'Movies C4Y90H',
1 'Dutch Names',
2 '15M1D',
3 'Movies C10Y2M',
4 'World Bank HIV',
5 'Movies 3y3M',
6 'GitHub standard',
7 'Movies HC9Y7M',
'Movies H22Y7M',
'Movies HC9Y1W',
'GitHub Hystrix'}
