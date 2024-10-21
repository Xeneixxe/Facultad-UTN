<script lang="js">
export class GetLocation {
  static async getData() {
    const response = await fetch('https://geolocation.microlink.io')
    const data = await response.json()
    return data
  }
  static async ip() {
    const data = await this.getData()
    return data.ip.address
  }
  static async country() {
    const data = await this.getData()
    return data.country.name
  }
  static async city() {
    const data = await this.getData()
    return data.city.name
  }
}
</script>