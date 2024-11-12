import axios from "axios";
import type { Job } from "$lib/types";

async function getJobs() {
  try {
    const response = await axios.get("/job");
  } catch (error) {
    console.error(error);
  }
}

async function getJob(job_id: string) {
  try {
    const response = await axios.post(`/job/${job_id}`);
  } catch (error) {
    console.error(error);
  }
}

async function createJob(job: Job) {
  try {
    const response = await axios.post("/job/create", job);
  } catch (error) {
    console.error(error);
  }
}

async function updateJob(job_id: string, job: Job) {
  try {
    const response = await axios.put(`/job/${job_id}`, job);
  } catch (error) {
    console.error(error);
  }
}

async function deleteJob(job_id: string) {
  try {
    const response = await axios.delete(`/job/${job_id}`);
  } catch (error) {
    console.error(error);
  }
}
