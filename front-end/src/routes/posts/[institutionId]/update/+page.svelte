<script lang="ts">
    import { getInstitution, updateInstitution, type InstitutionParam } from '$lib/api/institution'; // Adjust the import path as necessary
    import { onMount } from 'svelte';
  
    let institution_id: number;
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
    <input type="number" bind:value={institution_id} placeholder="Institution ID" required />
    <input type="number" bind:value={institutionData.no_of_employees} placeholder="Number of Employees" required />
    <input type="url" bind:value={institutionData.website} placeholder="Website" required />
    <input type="text" bind:value={institutionData.industry} placeholder="Industry" required />
    <input type="text" bind:value={institutionData.name} placeholder="Name" required />
    <input type="text" bind:value={institutionData.description} placeholder="Description" required />
    <input type="text" bind:value={institutionData.location_city} placeholder="City" required />
    <input type="text" bind:value={institutionData.location_state} placeholder="State" required />
    <input type="text" bind:value={institutionData.location_country} placeholder="Country" required />
    <button type="submit">Update Institution</button>
  </form>
  
  {#if message}
    <p>{message}</p>
  {/if}