package ServoControl;

public class Servo {
    public static void main(String[] args) {
        try {
            Runtime runtime = Runtime.getRuntime();
            runtime.exec("gpio mode 1 pwm");
            runtime.exec("gpio pwm-ms");
            runtime.exec("gpio pwmc 192");
            runtime.exec("gpio pwmr 2000");
            runtime.exec("gpio pwm 1 152");     //center

            Thread.sleep(5000);
            runtime.exec("gpio pwm 1 100");     //turn right
            Thread.sleep(3000);
            runtime.exec("gpio pwm 1 200");     //turn left
            Thread.sleep(3000);

            int i = 100;
            boolean turningLeft = true;
            while (true) {
                runtime.exec("gpio pwm 1 " + i);
                Thread.sleep(10);
                if (turningLeft) {
                    i++;
                } else {
                    i--;
                }
                if (i > 200) {
                    turningLeft = false;
                }
                if (i < 100) {
                    turningLeft = true;
                }
            }
        } catch (Exception e) {
            System.out.println("Exception occured: " + e.getMessage());
        }
    }
}