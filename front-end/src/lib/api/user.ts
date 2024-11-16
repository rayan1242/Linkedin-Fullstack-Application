import axios from "axios";
import type { User } from "$lib/types";

export type UserParam = Omit<User, "user_id">;

export async function getUsers() {
  const response = await axios.get("http://localhost:3000/user");
  return response.data;
}

export async function getUser(user_id: string) {
  const response = await axios.post(`http://localhost:3000/user/${user_id}`);
  return response.data;
}

export async function createUser(user: UserParam) {
  const response = await axios.post("http://localhost:3000/user/create", user);
  return response.data;
}

export async function updateUser(user_id: string, user: UserParam) {
  const response = await axios.put(
    `http://localhost:3000/user/${user_id}`,
    user
  );
  return response.data;
}

export async function deleteUser(user_id: string) {
  const response = await axios.delete(`http://localhost:3000/user/${user_id}`);
  return response.data;
}
