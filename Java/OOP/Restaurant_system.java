import java.util.ArrayList;
import java.util.List;
class Menu{
    /*
     * Menu gồm: 
      - id
      - Time
      - list của food
      - list của giá food
    /*Thuộc tính .... */
}
class Restaurant{
    /*
     * Restaurant gồm: 
      - name
      - address
      - list của menu
      - hàm order(menu_id, list các food trong menu id đó) -> return tổng bill của order.
     */
    /*Thuộc tính .... */
    /*Phương thức:  */
    public int order(int menu_id, List<String> foods){
        int total_bill =0 ; 
        // Continue....
        return total_bill;
    }
}
public class Restaurant_system {
    public static void main(String args[]){
        Restaurant restaurant = new Restaurant(...);
        double total_bill = restaurant.order(1,new List<String>{"ca kho to","thit kho",...})
        System.out.println("Total bill of order is: "+total_bill);
    }
}
