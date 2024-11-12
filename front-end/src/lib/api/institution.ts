import axios from "axios";
import type { Institution } from "$lib/types";

async function getInstitutions() {
  try {
    const response = await axios.get("/institution");
  } catch (error) {
    console.error(error);
  }
}

async function getInstitution(institution_id: string) {
  try {
    const response = await axios.post(`/institution/${institution_id}`);
  } catch (error) {
    console.error(error);
  }
}

async function createInstitution(institution: Institution) {
  try {
    const response = await axios.post("/institution/create", institution);
  } catch (error) {
    console.error(error);
  }
}

async function updateInstitution(
  institution_id: string,
  institution: Institution
) {
  try {
    const response = await axios.put(
      `/institution/${institution_id}`,
      institution
    );
  } catch (error) {
    console.error(error);
  }
}

async function deleteInstitution(institution_id: string) {
  try {
    const response = await axios.delete(`/institution/${institution_id}`);
  } catch (error) {
    console.error(error);
  }
}
