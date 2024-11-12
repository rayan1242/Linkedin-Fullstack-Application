import axios from "axios";
import type { Skill } from "$lib/types";

async function getSkills() {
  try {
    const response = await axios.get("/skill");
  } catch (error) {
    console.error(error);
  }
}

async function getSkill(skill_id: string) {
  try {
    const response = await axios.post(`/skill/${skill_id}`);
  } catch (error) {
    console.error(error);
  }
}

async function createSkill(skill: Skill) {
  try {
    const response = await axios.post("/skill/create", skill);
  } catch (error) {
    console.error(error);
  }
}

async function updateSkill(skill_id: string, skill: Skill) {
  try {
    const response = await axios.put(`/skill/${skill_id}`, skill);
  } catch (error) {
    console.error(error);
  }
}

async function deleteSkill(skill_id: string) {
  try {
    const response = await axios.delete(`/skill/${skill_id}`);
  } catch (error) {
    console.error(error);
  }
}
