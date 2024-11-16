import axios from "axios";
import type { Experience } from "$lib/types";

const api = axios.create({
  baseURL: "http://localhost:3000",
});

export type ExperienceParams = Omit<Experience, "exp_id">;


async function getExperiences() {
  try {
    const response = await api.get("/experience");
  } catch (error) {
    console.error(error);
  }
}

export async function getExperience(experience_id: number) {
  try {
    const response = await api.post(`/experience/${experience_id}`);
    return response.data;
  } catch (error) {
    console.error(error);
    return { status: 'error', message: 'Error getting experience.' };
  }

}

export async function createExperience(experience: ExperienceParams) {
  try {
    const response = await api.post("/experience/create", experience);
    return response.data;
  } catch (error) {
    console.error(error);
    return { status: 'error', message: 'Error creating experience.' };
  }
}

export async function updateExperience(experience_id: number, experience: ExperienceParams) {
  try {
    const response = await api.put(
      `/experience/${experience_id}`,
      experience
    );
    return  response.data;
  } catch (error) {
    console.error(error);
    return { status: 'error', message: 'Error updating experience.' };
  }
}

export async function deleteExperience(experience_id: number) {
  try {
    const response = await api.delete(`/experience/${experience_id}`);
    return response.data;
  } catch (error) {
    console.error(error);
    return { status: 'error', message: 'Error deleting experience.' };
  }
}
