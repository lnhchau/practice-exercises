import java.util.ArrayList;

/**
 * Abstract class representing a generic shape.
 */
abstract class Shape {

    /**
     * Abstract method to get the area of the shape.
     *
     * @return The area of the shape.
     */
    protected abstract double getArea();

    /**
     * Abstract method to get the perimeter of the shape.
     *
     * @return The perimeter of the shape.
     */
    protected abstract double getPerimeter();

    /**
     * Prints information about the shape, including its area and perimeter.
     */
    protected void getInfo() {
        // continue
    }
}

/**
 * Class representing a rectangle, a specific type of shape.
 */
class Rectangle extends Shape {

    private double width;
    private double height;

    /**
     * Constructor for the Rectangle class.
     *
     * @param width  The width of the rectangle.
     * @param height The height of the rectangle.
     */
    public Rectangle(double width, double height) {
    }

    /**
     * Calculates and returns the area of the rectangle.
     *
     * @return The area of the rectangle.
     */
    public double getArea() {
        // continue
        return 0;
    }

    /**
     * Calculates and returns the perimeter of the rectangle.
     *
     * @return The perimeter of the rectangle.
     */
    public double getPerimeter() {
        // continue
        return 0;
    }
}

/**
 * Class representing a square, a specific type of shape.
 */
class Square extends Shape {

    private double side;

    /**
     * Constructor for the Square class.
     *
     * @param side The side length of the square.
     */
    public Square(double side) {
        // continue
    }

    /**
     * Calculates and returns the area of the square.
     *
     * @return The area of the square.
     */
    public double getArea() {
        // continue
        return 0;
    }

    /**
     * Calculates and returns the perimeter of the square.
     *
     * @return The perimeter of the square.
     */
    public double getPerimeter() {
        // continue
        return 0;
    }
}

/**
 * Main class demonstrating the Shape system.
 */
public class Shape_system {

    /**
     * Main method to create shapes and print their information.
     *
     * @param args Command-line arguments (not used in this example).
     */
    public static void main(String args[]) {
        ArrayList<Shape> shapes = new ArrayList<Shape>();
        shapes.add(new Rectangle(5.0, 3.0));
        shapes.add(new Square(4.0));
        shapes.add(new Rectangle(1.0, 2.0));

        for (int i = 0; i < shapes.size(); i++) {
            shapes.get(i).getInfo();
        }
    }
}