<script lang="ts">
    import { getInstitution, updateInstitution, type InstitutionParam } from '$lib/api/institution'; // Adjust the import path as necessary
    import { onMount } from 'svelte';
  
    let institution_id: string;
    let institutionData = {
        institution_id: 0,   
      no_of_employees: 0,
      website: '',
      industry: '',
      name: '',
      description: '',
      location_city: '',
      location_state: '',
      location_country: ''
    };
  
    let message = '';
  
    onMount(async () => {
      try {
        const institution = await getInstitution(institution_id);
        institutionData = institution;
      } catch (e: any) {
        console.log(e);
      }
    });
  
    const handleSubmit = async () => {
      try {
        const response = await updateInstitution(institution_id, institutionData);
        if (response.status === 'success') {
          message = 'Institution updated successfully!';
        } else {
          message = `Error: ${response.message}`;
        }
      } catch (error) {
        console.error(error);
        message = 'Error updating institution.';
      }
    };
  </script>
  
  <form on:submit|preventDefault={handleSubmit}>
    <input type="number" bind:value={institution_id} placeholder="Institution ID"  />
    <input type="number" bind:value={institutionData.no_of_employees} placeholder="Number of Employees"  />
    <input type="url" bind:value={institutionData.website} placeholder="Website"  />
    <input type="text" bind:value={institutionData.industry} placeholder="Industry"  />
    <input type="text" bind:value={institutionData.name} placeholder="Name"  />
    <input type="text" bind:value={institutionData.description} placeholder="Description"  />
    <input type="text" bind:value={institutionData.location_city} placeholder="City"  />
    <input type="text" bind:value={institutionData.location_state} placeholder="State"  />
    <input type="text" bind:value={institutionData.location_country} placeholder="Country"  />
    <button type="submit">Update Institution</button>
  </form>
  
  {#if message}
    <p>{message}</p>
  {/if}

  <style>
    form {
      display: flex;
      flex-direction: column;
      max-width: 600px;
      margin: 0 auto;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 8px;
      background-color: #f9f9f9;
    }
  
    input, button {
      margin-bottom: 15px;
      padding: 10px;
      font-size: 16px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
  
    input:focus {
      border-color: #007BFF;
      outline: none;
    }
  
    button {
      background-color: #007BFF;
      color: white;
      cursor: pointer;
      border: none;
    }
  
    button:hover {
      background-color: #0056b3;
    }
  
    p {
      text-align: center;
      font-size: 18px;
      color: green;
    }
  </style>
  