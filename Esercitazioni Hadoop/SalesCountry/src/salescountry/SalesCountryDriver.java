package salescountry;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;

public class SalesCountryDriver {
    public static void main(String[] args) {
        JobClient client = new JobClient();
        // Create a configuration object for the job
        JobConf conf = new JobConf(SalesCountryDriver.class);

        // Set a name of the Job
        conf.setJobName("SalePerCountry");

        // Specify data type of output key and value
        conf.setOutputKeyClass(Text.class);
        conf.setOutputValueClass(IntWritable.class);

        // Specify names of Mapper and Reducer Class
        conf.setMapperClass(salescountry.SalesMapper.class);
        conf.setReducerClass(salescountry.SalesCountryReducer.class);

        // Specify formats of the data type of Input and output
        conf.setInputFormat(TextInputFormat.class);
        conf.setOutputFormat(TextOutputFormat.class);

        // Set input and output directories using command line arguments, 
        // arg[0] = name of input directory on HDFS, 
        // and arg[1] =  name of output directory to be created to store the output file.

        FileInputFormat.setInputPaths(conf, new Path(args[0]));
        FileOutputFormat.setOutputPath(conf, new Path(args[1]));

        client.setConf(conf);
        try {
            // Run the job 
            JobClient.runJob(conf);
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                client.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}
