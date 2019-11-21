//package org.glucosio.android.tools;

//import GlucosioConverter.java;
/**
 * Write a description of class Steve_Driver here.
 *
 * @author Boop
 * @version 
 */
public class Steve_DriverF {
	    

	    /**
	     * Constructor for objects of class Steve_Driver
	     */
	    public Steve_DriverF()
	    {
	        
	    }

	    public static void main(String args[]){
	    
	        String methodName = args[0];
	        double argument = Double.parseDouble(args[1]);
	        //double out = -1.0;
		Object out;
	        int argument2;
	        switch (methodName) {
	            
	            default:
	            	//argument2=Integer.parseInt(args[2]);
	                //out = GlucosioConverterF.round(argument,2);
			out= "invalid method called";
	                break;
	                
	            case "round":
	            	//argument2=Integer.parseInt(args[2]);
	                out = GlucosioConverterF.round(argument,2);
			
	                break;
	                
	            case "glucoseToMgDl":
	            
	                out = GlucosioConverterF.glucoseToMgDl(argument);
	                break;
	                
	            case "glucoseToMmolL":
	            
	                out = GlucosioConverterF.glucoseToMmolL(argument);
			
	                break;
	                
	            case "glucoseToA1C": 
	            
	                out = GlucosioConverterF.glucoseToA1C(argument);
			
	                break;
	                
	            case "a1cToGlucose":
	            
	                out = GlucosioConverterF.a1cToGlucose(argument);
			
	                break;
	        
	            }
	            
	            System.out.println(out);

	    }
}

