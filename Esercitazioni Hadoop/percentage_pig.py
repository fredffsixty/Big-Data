from pig_util import outputSchema;

@outputSchema("perc: double")
def percentage(num, total):
	return num*100/total;
