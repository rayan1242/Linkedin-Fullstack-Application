import axios from "axios";
import type { Application } from "$lib/types";

type ApplicationParam = Pick<
  Application,
  "user_id" | "job_id" | "application_status" | "application_date"
>;

export async function getApplications(): Promise<Application> {
  const response = await axios.get("http://localhost:3000/application");
  return response.data;
}

export async function getApplication(
  application_id: string
): Promise<Application> {
  const response = await axios.post(
    `http://localhost:3000/application/${application_id}`
  );
  return response.data;
}

export async function createApplication(
  applicationParam: ApplicationParam
): Promise<Application> {
  const response = await axios.post(
    "http://localhost:3000/application/create",
    applicationParam
  );
  return response.data;
}

export async function updateApplication(
  application_id: string,
  application: Application
): Promise<Application> {
  const response = await axios.put(
    `http://localhost:3000/application/${application_id}`,
    application
  );
  return response.data;
}

export async function deleteApplication(application_id: string) {
  const response = await axios.delete(
    `http://localhost:3000/application/${application_id}`
  );
  return response.data;
}
