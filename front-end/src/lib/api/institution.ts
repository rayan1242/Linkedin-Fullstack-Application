import axios from "axios";
import type { Institution } from "$lib/types";

const api = axios.create({
  baseURL: "http://localhost:3000",
});
export type InstitutionParam = Omit<Institution, "institution_id">;

async function getInstitutions() {
  try {
    const response = await api.get("/institution");
  } catch (error) {
    console.error(error);
  }
}

export async function getInstitution(institution_id: number) {
  try {
    const response = await api.post(`/institution/${institution_id}`);
    return response.data;
  } catch (error) {
    console.error(error);
    return { status: 'error', message: 'Error getting institution.' };
  }
}

export async function createInstitution(institution: InstitutionParam) {
  try {
    const response = await api.post("/institution/create", institution);
    return response.data;
  } catch (error) {
    console.error(error);
  }
}

export async function updateInstitution(
  institution_id: number,
  institution: Institution
) {
  try {
    const response = await api.put(
      `/institution/${institution_id}`,
      institution
    );
    return response.data; 
  } catch (error) {
    console.error(error);
    return { status: 'error', message: 'Error updating institution.' };
  }
}

export async function deleteInstitution(institution_id: number) {
  try {
    const response = await api.delete(`/institution/${institution_id}`);
    return response.data;
  } catch (error) {
    console.error(error);
    return { status: 'error', message: 'Error deleting institution.' };
  }
}
