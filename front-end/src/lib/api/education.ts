import axios from "axios";
import type { Education } from "$lib/types";

export async function getEducations() {
  const response = await axios.get("http://localhost:3000/education");
  return response.data;
}

export async function getEducation(education_id: string) {
  const response = await axios.post(
    `http://localhost:3000/education/${education_id}`
  );
  return response.data;
}

export async function createEducation(education: Education) {
  const response = await axios.post(
    "http://localhost:3000/education/create",
    education
  );
  return response.data;
}

export async function updateEducation(
  education_id: string,
  education: Education
) {
  const response = await axios.put(
    `http://localhost:3000/education/${education_id}`,
    education
  );
  return response.data;
}

export async function deleteEducation(education_id: string) {
  const response = await axios.delete(
    `http://localhost:3000/education/${education_id}`
  );
  return response.data;

}
