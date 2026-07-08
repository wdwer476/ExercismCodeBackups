// Package weather provides forecast information for cities in Goblinocus,
// including the current weather condition and location.
package weather

var (
	// CurrentCondition represents the current weather condition, such as
	// "sunny", "rainy", or "cloudy", for the most recently forecasted city.
	CurrentCondition string
	// CurrentLocation represents the name of the city for which the
	// current weather condition was most recently forecasted.
	CurrentLocation string
)

// Forecast returns a string describing the current weather condition
// of a given city.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}