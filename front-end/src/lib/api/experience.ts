import axios from "axios";
import type { Experience } from "$lib/types";

async function getExperiences() {
  try {
    const response = await axios.get("/experience");
  } catch (error) {
    console.error(error);
  }
}

async function getExperience(experience_id: string) {
  try {
    const response = await axios.post(`/experience/${experience_id}`);
  } catch (error) {
    console.error(error);
  }
}

async function createExperience(experience: Experience) {
  try {
    const response = await axios.post("/experience/create", experience);
  } catch (error) {
    console.error(error);
  }
}

async function updateExperience(experience_id: string, experience: Experience) {
  try {
    const response = await axios.put(
      `/experience/${experience_id}`,
      experience
    );
  } catch (error) {
    console.error(error);
  }
}

async function deleteExperience(experience_id: string) {
  try {
    const response = await axios.delete(`/experience/${experience_id}`);
  } catch (error) {
    console.error(error);
  }
}
