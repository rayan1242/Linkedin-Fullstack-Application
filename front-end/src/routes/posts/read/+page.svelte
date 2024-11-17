<script lang="ts">
    import { getInstitution } from '$lib/api/institution'; // Adjust the import path as necessary
  
    let institution_id: number;
    let message = '';
    let institution: {
      institution_id?: number;
      no_of_employees?: number;
      website?: string;
      industry?: string;
      name?: string;
      description?: string;
      location_city?: string;
      location_state?: string;
      location_country?: string;
    } = {};
  
    const handleSubmit = async () => {
      try {
        const response = await getInstitution(institution_id);
        if (response.status === 'success') {
          institution = response.institution;
          message = '';
        } else {
          message = `Error: ${response.message}`;
          institution = {};
        }
      } catch (error) {
        console.error(error);
        message = 'Error fetching institution.';
        institution = {};
      }
    };
  </script>
  
  <form on:submit|preventDefault={handleSubmit}>
    <input type="number" bind:value={institution_id} placeholder="Institution ID" />
    <button type="submit">Get Institution</button>
  </form>
  
  {#if message}
    <p>{message}</p>
  {/if}
  
  {#if institution.institution_id}
    <div>
      <h2>Institution Details</h2>
      <p><strong>ID:</strong> {institution.institution_id}</p>
      <p><strong>Number of Employees:</strong> {institution.no_of_employees}</p>
      <p><strong>Website:</strong> {institution.website}</p>
      <p><strong>Industry:</strong> {institution.industry}</p>
      <p><strong>Name:</strong> {institution.name}</p>
      <p><strong>Description:</strong> {institution.description}</p>
      <p><strong>City:</strong> {institution.location_city}</p>
      <p><strong>State:</strong> {institution.location_state}</p>
      <p><strong>Country:</strong> {institution.location_country}</p>
    </div>
  {/if}