import axios from "axios";
import type { Skill } from "$lib/types";

const api = axios.create({
  baseURL: "http://localhost:3000",
});

export type skillParam = Omit<Skill, "skill_id">;


async function getSkills() {
  try {
    const response = await api.get("/skill");
  } catch (error) {
    console.error(error);
  }
}

export async function getSkill(skill_id: number) {
  try {
    const response = await api.post(`/skill/${skill_id}`);
  } catch (error) {
    console.error(error);
  }
}

export async function createSkill(skill: skillParam) {
  try {
    const response = await api.post("/skill/create", skill);
  } catch (error) {
    console.error(error);
  }
}

export async function updateSkill(skill_id: number, skill: skillParam) {
  try {
    const response = await api.put(`/skill/${skill_id}`, skill);
  } catch (error) {
    console.error(error);
  }
}

export async function deleteSkill(skill_id: number) {
  try {
    const response = await api.delete(`/skill/${skill_id}`);
  } catch (error) {
    console.error(error);
  }
}
