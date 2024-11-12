import axios from "axios";
import type { Application } from "$lib/types";

async function getApplications() {
  try {
    const response = await axios.get("/application");
  } catch (error) {
    console.error(error);
  }
}

async function getApplication(application_id: string) {
  try {
    const response = await axios.post(`/application/${application_id}`);
  } catch (error) {
    console.error(error);
  }
}

async function createApplication(application: Application) {
  try {
    const response = await axios.post("/application/create", application);
  } catch (error) {
    console.error(error);
  }
}

async function updateApplication(
  application_id: string,
  application: Application
) {
  try {
    const response = await axios.put(
      `/application/${application_id}`,
      application
    );
  } catch (error) {
    console.error(error);
  }
}

async function deleteApplication(application_id: string) {
  try {
    const response = await axios.delete(`/application/${application_id}`);
  } catch (error) {
    console.error(error);
  }
}
