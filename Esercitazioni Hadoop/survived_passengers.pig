-- register 'percentage_pig.py' using streaming_python as myfuncs;
-- register 'percentage_pig.js' using javascript as myfuncs;

titanic = load 'hdfs://localhost/InputMapReduce/titanic_qualified.csv' using PigStorage() as (id:int, survived:int, class:int, name:chararray, sex:chararray,age:int, sibsp:int, parch:int, ticket:chararray, fare:double, cabin:chararray, embarked:chararray);

embarked = group titanic by (sex,class);

embarked_totals = FOREACH embarked GENERATE $0, COUNT(titanic);

survived = filter titanic by survived == 1;

survived_grouped = group survived by (sex,class);

embarked_survived = JOIN survived_grouped BY $0, embarked_totals BY $0;

survived_counts = FOREACH embarked_survived GENERATE $0, COUNT(survived), (float)COUNT(survived)*100.0/(float)$3, AVG(survived.age);

-- survived_stats = FOREACH survived_counts GENERATE $0, $1, myfuncs.percentage($1,$2), $3;

store survived_counts into 'hdfs://localhost/output_map_reduce/survived_stats' using PigStorage();
