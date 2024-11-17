import axios from "axios";
import type { User } from "../types";

const api = axios.create({
  baseURL: "http://localhost:3000",
});

export type UserParam = Omit<User, "user_id">;

export async function getUsers() {
  const response = await api.get("/user");
  return response.data;
}

export async function getUser(user_id: number) {
  const response = await api.post(`/user/${user_id}`);

  return response.data;
}

export async function createUser(user: UserParam) {
  const response = await api.post("/user/create", user);
  return response.data;
}

export async function updateUser(user_id: number, user: UserParam) {
  const response = await api.put(`/user/${user_id}`, user);
  return response.data;
}

export async function deleteUser(user_id: number) {
  const response = await api.delete(`/user/${user_id}`);

  return response.data;
}
