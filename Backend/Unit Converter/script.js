// Unit conversion data and functions
const conversionData = {
    length: {
        units: ['millimeter', 'centimeter', 'meter', 'kilometer', 'inch', 'foot', 'yard', 'mile'],
        conversions: {
            // Base unit: meter
            millimeter: 0.001,
            centimeter: 0.01,
            meter: 1,
            kilometer: 1000,
            inch: 0.0254,
            foot: 0.3048,
            yard: 0.9144,
            mile: 1609.344
        }
    },
    weight: {
        units: ['milligram', 'gram', 'kilogram', 'ounce', 'pound'],
        conversions: {
            // Base unit: kilogram
            milligram: 0.000001,
            gram: 0.001,
            kilogram: 1,
            ounce: 0.0283495,
            pound: 0.453592
        }
    },
    temperature: {
        units: ['Celsius', 'Fahrenheit', 'Kelvin'],
        conversions: {
            // Special handling for temperature
            Celsius: 'C',
            Fahrenheit: 'F',
            Kelvin: 'K'
        }
    }
};

// DOM elements
const categoryBtns = document.querySelectorAll('.category-btn');
const fromUnitSelect = document.getElementById('fromUnit');
const toUnitSelect = document.getElementById('toUnit');
const inputValue = document.getElementById('inputValue');
const convertBtn = document.getElementById('convertBtn');
const resultDisplay = document.getElementById('resultDisplay');
const resultValue = document.getElementById('resultValue');
const resetBtn = document.getElementById('resetBtn');
const categoryText = document.querySelector('.category-text');

let currentCategory = 'length';

// Initialize the application
function init() {
    populateUnitSelects();
    addEventListeners();
    updateCategoryText();
}

// Populate unit select dropdowns
function populateUnitSelects() {
    const units = conversionData[currentCategory].units;
    
    // Clear existing options
    fromUnitSelect.innerHTML = '';
    toUnitSelect.innerHTML = '';
    
    // Add options to both selects
    units.forEach(unit => {
        const fromOption = document.createElement('option');
        fromOption.value = unit;
        fromOption.textContent = unit.charAt(0).toUpperCase() + unit.slice(1);
        fromUnitSelect.appendChild(fromOption);
        
        const toOption = document.createElement('option');
        toOption.value = unit;
        toOption.textContent = unit.charAt(0).toUpperCase() + unit.slice(1);
        toUnitSelect.appendChild(toOption);
    });
    
    // Set default selections (different units)
    if (units.length > 1) {
        fromUnitSelect.selectedIndex = 0;
        toUnitSelect.selectedIndex = 1;
    }
}

// Add event listeners
function addEventListeners() {
    // Category button clicks
    categoryBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            switchCategory(btn.dataset.category);
        });
    });
    
    // Convert button click
    convertBtn.addEventListener('click', performConversion);
    
    // Reset button click
    resetBtn.addEventListener('click', resetForm);
    
    // Input value change
    inputValue.addEventListener('input', () => {
        if (resultDisplay.style.display !== 'none') {
            resultDisplay.style.display = 'none';
        }
    });
}

// Switch between categories
function switchCategory(category) {
    currentCategory = category;
    
    // Update active button
    categoryBtns.forEach(btn => {
        btn.classList.remove('active');
        if (btn.dataset.category === category) {
            btn.classList.add('active');
        }
    });
    
    // Update category text
    updateCategoryText();
    
    // Repopulate unit selects
    populateUnitSelects();
    
    // Hide result display
    resultDisplay.style.display = 'none';
    
    // Clear input
    inputValue.value = '';
}

// Update category text in label
function updateCategoryText() {
    categoryText.textContent = currentCategory;
}

// Perform unit conversion
function performConversion() {
    const value = parseFloat(inputValue.value);
    const fromUnit = fromUnitSelect.value;
    const toUnit = toUnitSelect.value;
    
    if (isNaN(value)) {
        alert('Please enter a valid number');
        return;
    }
    
    if (fromUnit === toUnit) {
        alert('Please select different units to convert between');
        return;
    }
    
    let result;
    
    if (currentCategory === 'temperature') {
        result = convertTemperature(value, fromUnit, toUnit);
    } else {
        result = convertStandard(value, fromUnit, toUnit);
    }
    
    // Display result
    displayResult(value, fromUnit, result, toUnit);
}

// Convert standard units (length, weight)
function convertStandard(value, fromUnit, toUnit) {
    const data = conversionData[currentCategory];
    const fromFactor = data.conversions[fromUnit];
    const toFactor = data.conversions[toUnit];
    
    // Convert to base unit, then to target unit
    const baseValue = value * fromFactor;
    return baseValue / toFactor;
}

// Convert temperature units
function convertTemperature(value, fromUnit, toUnit) {
    let celsius;
    
    // Convert to Celsius first
    switch (fromUnit) {
        case 'Celsius':
            celsius = value;
            break;
        case 'Fahrenheit':
            celsius = (value - 32) * 5/9;
            break;
        case 'Kelvin':
            celsius = value - 273.15;
            break;
    }
    
    // Convert from Celsius to target unit
    switch (toUnit) {
        case 'Celsius':
            return celsius;
        case 'Fahrenheit':
            return (celsius * 9/5) + 32;
        case 'Kelvin':
            return celsius + 273.15;
    }
}

// Display conversion result
function displayResult(inputValue, fromUnit, result, toUnit) {
    // Format result based on category
    let formattedResult;
    if (currentCategory === 'temperature') {
        formattedResult = `${inputValue}°${fromUnit.charAt(0)} = ${result.toFixed(2)}°${toUnit.charAt(0)}`;
    } else {
        formattedResult = `${inputValue} ${fromUnit} = ${result.toFixed(4)} ${toUnit}`;
    }
    
    resultValue.textContent = formattedResult;
    resultDisplay.style.display = 'block';
}

// Reset the form
function resetForm() {
    inputValue.value = '';
    resultDisplay.style.display = 'none';
    populateUnitSelects();
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', init);
