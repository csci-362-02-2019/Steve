
/**
 * Write a description of class Steve_Driver here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Steve_Driver
{
    
    

    /**
     * Constructor for objects of class Steve_Driver
     */
    public Steve_Driver()
    {
        
    }

    public static void main(String args[]){
    
        String methodName = args[0];
        double argument = Double.parseDouble(args[1]);
        double out = -1.0;
        
        switch (methodName) {
            
            default:
            
                out = GlucosioConverter.round(argument);
                break;
                
            case "round":
            
                out = GlucosioConverter.round(argument);
                break;
                
            case "glucoseToMgDl":
            
                out = GlucosioConverter.glucoseToMgDl(argument);
                break;
                
            case "glucoseToMmolL":
            
                out = GlucosioConverter.glucoseToMmolL(argument);
                break;
                
            case "glucoseToA1C": 
            
                out = GlucosioConverter.glucoseToMmolL(argument);
                break;
                
            case "a1cToGlucose":
            
                out = GlucosioConverter.glucosea1cToGlucose(argument);
                break;
        
            }
            
            System.out.print(out);
    }
}
