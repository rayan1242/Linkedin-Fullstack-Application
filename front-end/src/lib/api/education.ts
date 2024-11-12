import axios from "axios";
import type { Education } from "$lib/types";

async function getEducations() {
  try {
    const response = await axios.get("/education");
  } catch (error) {
    console.error(error);
  }
}

async function getEducation(education_id: string) {
  try {
    const response = await axios.post(`/education/${education_id}`);
  } catch (error) {
    console.error(error);
  }
}

async function createEducation(education: Education) {
  try {
    const response = await axios.post("/education/create", education);
  } catch (error) {
    console.error(error);
  }
}

async function updateEducation(education_id: string, education: Education) {
  try {
    const response = await axios.put(`/education/${education_id}`, education);
  } catch (error) {
    console.error(error);
  }
}

async function deleteEducation(education_id: string) {
  try {
    const response = await axios.delete(`/education/${education_id}`);
  } catch (error) {
    console.error(error);
  }
}
