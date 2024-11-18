import axios from "axios";
import type { Education } from "$lib/types";

export type EducationParam = Omit<Education, "edu_id">;

export async function getEducations() {
  const response = await axios.get("http://localhost:3000/education");
  return response.data;
}

export async function getEducation(user_id: string) {
  const response = await axios.get(
    `http://localhost:3000/education/${user_id}`
  );
  console.log(response.data);
  return response.data;
}

export async function createEducation(education: EducationParam) {
  const response = await axios.post(
    "http://localhost:3000/education/create",
    education
  );
  return response.data;
}

export async function updateEducation(
  edu_id: string,
  education: EducationParam
) {
  const response = await axios.put(
    `http://localhost:3000/education/${edu_id}`,
    education
  );
  return response.data;
}

export async function deleteEducation(edu_id: string) {
  const response = await axios.delete(
    `http://localhost:3000/education/${edu_id}`
  );
  return response.data;
}
