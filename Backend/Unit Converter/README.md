# Unit Converter Web Application

A simple, modern web application that converts between different units of measurement. Built with HTML, CSS, and JavaScript.

## Features

- **Multiple Unit Categories**: Convert between units in three main categories:
  - **Length**: millimeter, centimeter, meter, kilometer, inch, foot, yard, mile
  - **Weight**: milligram, gram, kilogram, ounce, pound
  - **Temperature**: Celsius, Fahrenheit, Kelvin

- **User-Friendly Interface**: Clean, responsive design that works on both desktop and mobile devices
- **Real-time Conversion**: Instant conversion results with proper formatting
- **Category Switching**: Easy switching between different unit types
- **Input Validation**: Ensures valid input and prevents conversion errors

## How to Use

1. **Select a Category**: Click on one of the category buttons (Length, Weight, or Temperature)
2. **Enter Value**: Type the value you want to convert in the input field
3. **Choose Units**: Select the unit you're converting from and the unit you're converting to
4. **Convert**: Click the "Convert" button to see the result
5. **Reset**: Use the "Reset" button to clear the form and start over

## Supported Conversions

### Length Units
- **Metric**: millimeter, centimeter, meter, kilometer
- **Imperial**: inch, foot, yard, mile

### Weight Units
- **Metric**: milligram, gram, kilogram
- **Imperial**: ounce, pound

### Temperature Units
- **Celsius** (°C)
- **Fahrenheit** (°F)
- **Kelvin** (K)

## How It Works

The application uses conversion factors and mathematical formulas to convert between units:

- **Length & Weight**: Uses base unit conversion (meter for length, kilogram for weight)
- **Temperature**: Uses standard temperature conversion formulas (Celsius as the base unit)

## Technical Details

- **Frontend**: Pure HTML, CSS, and JavaScript
- **No Dependencies**: Runs entirely in the browser
- **Responsive Design**: Works on all screen sizes
- **Modern CSS**: Uses CSS Grid, Flexbox, and modern styling techniques

## Getting Started

1. Download or clone the project files
2. Open `index.html` in your web browser
3. Start converting units!

## File Structure

```
unit-converter/
├── index.html          # Main HTML file
├── styles.css          # CSS styling
├── script.js           # JavaScript functionality
└── README.md           # This file
```

## Browser Compatibility

- Chrome (recommended)
- Firefox
- Safari
- Edge
- Internet Explorer 11+

## Future Enhancements

Potential features that could be added:
- More unit categories (area, volume, speed, etc.)
- History of conversions
- Favorite conversions
- Unit abbreviations
- Scientific notation support
- Dark mode toggle

## License

This project is open source and available under the MIT License.
