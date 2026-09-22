public class CarsAssemble 
{

    public double productionRatePerHour(int speed) 
    {
        if(speed >= 1 && speed <= 4)
        {
            return (double )speed * 221;
        }

        else if(speed >= 5 && speed <= 8)
        {
            return (double) speed * 221 * 0.9;
        }

        else if(speed == 9)
        {
            return (double) speed * 221 * 0.8;
        }

        else
        {
            return (double) speed * 221 * 0.77;
        }
    }

    public int workingItemsPerMinute(int speed) 
    {
        return (int) productionRatePerHour(speed) / 60;
    }
}
