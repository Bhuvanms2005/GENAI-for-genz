const BASE_URL = "http://127.0.0.1:8000/chat";

export async function fetchSummary() {
  const res = await fetch(`${BASE_URL}/summary`);
  return res.json();
}

export async function fetchNutrition() {
  const res = await fetch(`${BASE_URL}/nutrition`);
  return res.json();
}

export async function fetchExercise() {
  const res = await fetch(`${BASE_URL}/exercise`);
  return res.json();
}

export async function fetchSleep() {
  const res = await fetch(`${BASE_URL}/sleep`);
  return res.json();
}

export async function fetchGoals() {
  const res = await fetch(`${BASE_URL}/goals`);
  return res.json();
}

export async function fetchDoctor() {
  const res = await fetch(`${BASE_URL}/doctor`);
  return res.json();
}

export async function fetchAnomalies() {
  const res = await fetch(`${BASE_URL}/anomalies`);
  return res.json();
}

export async function fetchProgress() {
  const res = await fetch(`${BASE_URL}/progress`);
  return res.json();
}
