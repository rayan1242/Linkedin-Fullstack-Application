import axios from "axios";
import type { Skill } from "$lib/types";

export async function getSkills() {
  const response = await axios.get("http://localhost:3000/skill");
  return response.data;
}

export async function getSkill(skill_id: string) {
  const response = await axios.post(`http://localhost:3000/skill/${skill_id}`);
  return response.data;
}

export async function createSkill(skill: Skill) {
  const response = await axios.post(
    "http://localhost:3000/skill/create",
    skill
  );
  return response.data;
}

export async function updateSkill(skill_id: string, skill: Skill) {
  const response = await axios.put(
    `http://localhost:3000/skill/${skill_id}`,
    skill
  );
  return response.data;
}

export async function deleteSkill(skill_id: string) {
  const response = await axios.delete(
    `http://localhost:3000/skill/${skill_id}`
  );
  return response.data;

}
