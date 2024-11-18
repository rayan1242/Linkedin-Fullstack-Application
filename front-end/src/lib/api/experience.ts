import axios from "axios";
import type { Experience } from "$lib/types";

const api = axios.create({
  baseURL: "http://localhost:3000",
});

export type ExperienceParams = Omit<Experience, "exp_id">;


export async function getExperiences() {
  const response = await axios.get("http://localhost:3000/experience");
  return response.data;
}

export async function getExperience(experience_id: string) {
  const response = await axios.get(
    `http://localhost:3000/experience/${experience_id}`
  );
  return response.data;
}

export async function createExperience(experience: ExperienceParams) {
  const response = await axios.post(
    "http://localhost:3000/experience/create",
    experience
  );
  return response.data;
}

export async function updateExperience(experience_id: string, experience: ExperienceParams) {
  const response = await axios.put(
    `http://localhost:3000/experience/${experience_id}`,
    experience
  );
  return response.data;
}

export async function deleteExperience(experience_id: string) {
  const response = await axios.delete(
    `http://localhost:3000/experience/${experience_id}`
  );
  return response.data;
 
}
