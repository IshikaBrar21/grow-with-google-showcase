import { useState } from "react";
import "./App.css";

function App() {
  const [city, setCity] = useState("");
  const [gardenSize, setGardenSize] = useState("Small");
  const [sunlight, setSunlight] = useState("Full Sun");
  const [maintenance, setMaintenance] = useState("Low");
  const [hasSearched, setHasSearched] = useState(false);

  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();
    // Handle form submission logic here
    setLoading(true);
    setError("");
    try {
      const response = await fetch("http://127.0.0.1:8000/recommend", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          city: city,
          garden_size: gardenSize,
          sunlight: sunlight,
          maintenance: maintenance,
        }),
      });
    if (!response.ok){
      throw new Error("Network response was not ok");
    }
  
    const data  = await response.json();
    setRecommendations(data.recommendations);
    setHasSearched(true);
    }
    catch (error) {
      setError(error.message);
      setRecommendations([]);
    }
    finally{
      setLoading(false);
    }

  };
  return (
    <div className="app">
      <main className="planner">
        <h1>Biodiversity & Native Planting Planner</h1>

        <p className="subtitle">
          Find native plants that support local pollinators.
        </p>

        <form onSubmit={handleSubmit}>
          <label>
            Location
            <input
              type="text"
              value={city}
              onChange={(event) => setCity(event.target.value)}
              placeholder="Enter your city"
            />
          </label>

          <label>
            Garden Size
            <select
              value={gardenSize}
              onChange={(event) => setGardenSize(event.target.value)}
            >
              <option>Small</option>
              <option>Medium</option>
              <option>Large</option>
            </select>
          </label>

          <label>
            Sunlight
            <select
              value={sunlight}
              onChange={(event) => setSunlight(event.target.value)}
            >
              <option>Full Sun</option>
              <option>Part Sun</option>
              <option>Shade</option>
            </select>
          </label>

          <label>
            Maintenance
            <select
              value={maintenance}
              onChange={(event) => setMaintenance(event.target.value)}
            >
              <option>Low</option>
              <option>Medium</option>
              <option>High</option>
            </select>
          </label>

          <button type="submit">
            Find My Plants
          </button>
        </form>
        {loading && <p>Finding suitable native plants...</p>}

{error && <p className="error">{error}</p>}

{!loading && !error && recommendations.length > 0 && (
  <section className="results">
    <h2>Recommended Plants</h2>

    <div className="plant-list">
      {recommendations.map((plant) => (
        <article className="plant-card" key={plant.species_id}>
          <h3>{plant.common_name}</h3>

          <p className="scientific-name">
            {plant.scientific_name}
          </p>

          <p>
            <strong>Bloom:</strong>{" "}
            {plant.bloom_start} – {plant.bloom_end}
          </p>

          <p>
            <strong>Sunlight:</strong> {plant.sun_needs}
          </p>

          <p>
            <strong>Soil:</strong> {plant.soil_type}
          </p>

          <p>
            <strong>Moisture:</strong> {plant.moisture}
          </p>

          <p>
            <strong>Hardiness:</strong> {plant.hardiness_zones}
          </p>

          <p>
            <strong>Pollinators:</strong>{" "}
            {plant.pollinators_supported.join(", ")}
          </p>
        </article>
      ))}
    </div>
  </section>
)}
{!loading &&
  !error &&
  recommendations.length === 0 &&
  hasSearched && (
    <p className="empty-message">
      No suitable plants found for this location yet.
    </p>
  )}
      </main>
    </div>
  );
}

export default App;