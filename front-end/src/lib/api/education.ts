import axios from "axios";
import type { Education } from "$lib/types";

const api = axios.create({
  baseURL: "http://localhost:3000",
});

export type EducationParams = Omit<Education, "edu_id">;


export async function getEducations() {
  try {
    const response = await api.get("/education");
  } catch (error) {
    console.error(error);
  }
}

export async function getEducation(education_id: number) {
  try {
    const response = await api.post(`/education/${education_id}`);
    return response.data;
  } catch (error) {
    console.error(error);
    return { status: 'error', message: 'Error getting education.' };  
  }
}

export async function createEducation(education: EducationParams) {
  try {
    const response = await api.post("/education/create", education);
    return response.data;
  } catch (error) {
    console.error(error);
  }
}

export async function updateEducation(education_id: number, education: EducationParams) {
  try {
    const response = await api.put(`/education/${education_id}`, education);
    return response.data;
  } catch (error) {
    console.error(error);
    return { status: 'error', message: 'Error updating education.' };
  }
}

export async function deleteEducation(education_id: number) {
  try {
    const response = await api.delete(`/education/${education_id}`);
    return response.data; 
  } catch (error) {
    console.error(error);
    return { status: 'error', message: 'Error deleting education.' };
  }
}
