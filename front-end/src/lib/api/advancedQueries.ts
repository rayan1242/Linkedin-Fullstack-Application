import axios from "axios";
import type { advancedQuery } from "$lib/types";


export async function getUserPerformance() {
    const response = await axios.get("http://localhost:3000/advanced_queries/user_performance");
    return response.data;
  }


export async function getgrowthanalysis(){
    const response = await axios.get("http://localhost:3000/advanced_queries/growthAnalysis");
    return response.data;
}

export async function getJobRecommendations(user_id: string){
    const response = await axios.get(`http://localhost:3000/advanced_queries/getJobRecommendation/${user_id}`);
    return response.data;
}