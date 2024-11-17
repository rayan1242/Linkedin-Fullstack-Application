import axios from "axios";
import type { advancedQuery } from "$lib/types";


export async function getUserPerformance() {
    const response = await axios.get("http://localhost:3000/advanced_queries/user_performance");
    return response.data;
  }


export async function getgrowthanalysis(){
    const response = await axios.get("http://localhost:3000/advanced_queries/analyze_institution_growth");
    return response.data;
}

export async function getJobRecommendation(){
    const response = await axios.get("http://localhost:3000/advanced_queries/getJobRecommendation");
    return response.data;
}