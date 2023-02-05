const ContentBlock = ({title, content, style}) => {

  return (
    <div className={`contentBlock ${style}`}>
      <h2>{title}</h2>
      <div className="sixtyLine"></div>
      {content}
    </div>
  )
}

export default ContentBlock