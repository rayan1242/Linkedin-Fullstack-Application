import axios from "axios";
import type { Institution } from "$lib/types";

export type InstitutionParam = Omit<Institution, "institution_id">;


export async function getInstitutions() {
  const response = await axios.get("http://localhost:3000/institution");
  return response.data;
}

export async function getInstitution(institution_id: string) {
  const response = await axios.post(
    `http://localhost:3000/institution/${institution_id}`
  );
  return response.data;
}

export async function createInstitution(institution: InstitutionParam) {
  const response = await axios.post(
    "http://localhost:3000/institution/create",
    institution
  );
  return response.data;
}

export async function updateInstitution(
  institution_id: string,
  institution: InstitutionParam
) {
  const response = await axios.put(
    `http://localhost:3000/institution/${institution_id}`,
    institution
  );
  return response.data;
}

export async function deleteInstitution(institution_id: string) {
  const response = await axios.delete(
    `http://localhost:3000/institution/${institution_id}`
  );
  return response.data;

}
