import java.util.ArrayList;
import java.util.List;
import java.time.LocalTime;

/**
 * Represents a menu with an ID, time, list of foods, and corresponding prices.
 */
class Menu {
    private int id;
    private LocalTime time;
    private ArrayList<String> foods;
    private ArrayList<Double> prices;

    /**
     * Default constructor for the Menu class.
     */
    public Menu() {}

    /**
     * Constructs a menu with the specified ID, time, foods, and prices.
     *
     * @param id     The ID of the menu.
     * @param time   The time the menu is available.
     * @param foods  The list of foods available in the menu.
     * @param prices The corresponding prices for each food in the menu.
     */
    public Menu(int id, LocalTime time, ArrayList<String> foods, ArrayList<Double> prices) {

    }

    /**
     * Gets the ID of the menu.
     *
     * @return The ID of the menu.
     */
    public int getId() {
        return id;
    }

    /**
     * Gets the price of a specific food in the menu.
     *
     * @param food The name of the food.
     * @return The price of the specified food.
     */
    public double getPriceFood(String food) {
        double price = 0;
        // continue
        return price;
    }
}

/**
 * Represents a restaurant with a name, address, and a list of menus.
 */
class Restaurant {
    private String name;
    private String address;
    private ArrayList<Menu> menus;

    /**
     * Constructs a restaurant with the specified name, address, and menus.
     *
     * @param name    The name of the restaurant.
     * @param address The address of the restaurant.
     * @param menus   The list of menus available in the restaurant.
     */
    public Restaurant(String name, String address, ArrayList<Menu> menus) {

    }

    /**
     * Places an order in the restaurant and calculates the total bill.
     *
     * @param menuId The ID of the menu to order from.
     * @param foods  The list of foods to order.
     * @return The total bill for the order.
     */
    public double order(int menuId, List<String> foods) {
        double total_bill = 0;
        // Continue
        return total_bill;
    }
}

public class Restaurant_system {
    public static void main(String args[]){
        String restaurant_name = "OOP Class";
        String restaurant_addr = "VN";
        ArrayList<Menu> menus = new ArrayList<Menu>();
        
        Menu menu_1 = new Menu(
            1,
            LocalTime.of(8,0),
            new ArrayList<String>(){{
                add("hu tieu");
                add("com tam");
                add("bun bo");
            }},
            new ArrayList<Double>(){{
                add(45.0);
                add(55.0);
                add(45.0);
            }}
        );

        Menu menu_2 = new Menu(
            2,
            LocalTime.of(13,0),
            new ArrayList<String>(){{
                add("thit kho");
                add("ca kho");
                add("trung chien");
            }},
            new ArrayList<Double>(){{
                add(45.0);
                add(55.0);
                add(25.0);
            }}
        );
            
        menus.add(menu_1);
        menus.add(menu_2);
        Restaurant restaurant = new Restaurant(
            restaurant_name,
            restaurant_addr,
            menus
        );

        double total_bill = restaurant.order(2,new ArrayList<String>(){{
                add("thit kho");
                add("thit kho");
                add("trung chien");
            }});
        System.out.println("Total bill of order is: "+total_bill);
    }
}
